# Using Postgres
- Two Options:
    - Install directly onto your machine
    - Use Docker Container
    
### Installing Postgres 10 & pgAdmin4 via Docker
- [Easy PostgreSQL 10 and pgAdmin 4 Setup with Docker](https://info.crunchydata.com/blog/easy-postgresql-10-and-pgadmin-4-setup-with-docker)
- [Compose-Postgres Repo](https://github.com/khezen/compose-postgres)
- [Official Docker Postgres repo](https://hub.docker.com/_/postgres)
- [Docker Volumes](https://docs.docker.com/storage/volumes/)

### pg_dump of Postgres (DB Backup, Tables, etc)
- [How to backup a PostgreSQL database using Docker](https://devopsheaven.com/postgresql/pg_dump/databases/docker/backup/2017/09/10/backup-postgresql-database-using-docker.html)
- [Postgres Docs - pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)

# Postgres GUI Tool Needed
- I recommend using [pgadmin](https://www.pgadmin.org/)
- You can download and install this directly onto your machine or also run this in another docker container. I typically will install this directly on my machine, it's small (~ 100 MB).


### Postgres Full-Text Search
- [Mastering PostgreSQL Tools: Full-Text Search and Phrase Search](https://www.compose.com/articles/mastering-postgresql-tools-full-text-search-and-phrase-search/)
- [Postgres full-text search is Good Enough!](http://rachbelaid.com/postgres-full-text-search-is-good-enough/)
- [Fast Full-Text Search in PostgreSQL](https://austingwalters.com/fast-full-text-search-in-postgresql/)
