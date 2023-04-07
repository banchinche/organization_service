"""UUID generation function

Revision ID: 73b1aef2f7d3
Revises: 
Create Date: 2023-04-07 20:00:45.899742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73b1aef2f7d3'
down_revision = None
branch_labels = None
depends_on = None

"""
Upgrade & downgrade SQL-scripts
also can be found at src/infrastructure/db/functions/generate_uuid7
"""


def upgrade() -> None:
    op.execute("""
        CREATE OR REPLACE FUNCTION generate_uuid7()
        RETURNS uuid
        AS $$
        DECLARE
          unix_ts_ms bytea;
          uuid_bytes bytea;
        BEGIN
          unix_ts_ms = substring(int8send(floor(extract(epoch from clock_timestamp()) * 1000)::bigint) from 3);
        
          -- use random v4 uuid as starting point (which has the same variant we need)
          uuid_bytes = uuid_send(gen_random_uuid());
        
          -- overlay timestamp
          uuid_bytes = overlay(uuid_bytes placing unix_ts_ms from 1 for 6);
        
          -- set version 7
          uuid_bytes = set_byte(uuid_bytes, 6, (b'0111'|| get_byte(uuid_bytes, 6)::bit(4))::bit(8)::int);
        
          RETURN encode(uuid_bytes, 'hex')::uuid;
        END
        $$
        LANGUAGE plpgsql
        VOLATILE;
    """)


def downgrade() -> None:
    op.execute("DROP FUNCTION generate_uuid7;")
