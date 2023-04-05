# Organization Service

...Description...


# Installation

You need a `make` and `docker-compose` installed.

First create files `.env` and `config/local.config.toml`and/or `config/production.config.toml` 
(check config selection in the env-file) and fill in according to the example from 
corresponding templates (filenames contain `.template` before extension)

To up the containers, type

```
make run
```

Then, to apply migrations, type

```
make migrate
```

Finally, to shut down the containers, type

```
make down
```

Another make-commands you can discover [here](./Makefile).

# Dependencies

...Description...
