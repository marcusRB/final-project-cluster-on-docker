{
    "name": "postgres-datasource",
    "type": "postgres",
    "typeLogoUrl": "public/app/plugins/datasource/postgres/img/postgresql_logo.svg",
    "access": "proxy",
    "url": ${POSTGRES_HOST}:5432",
    "password": ${POSTGRES_PASSWORD},
    "user": ${POSTGRES_USER},
    "database": ${POSTGRES_DB} ,
    "basicAuth": false,
    "isDefault": true,
    "jsonData": {
        "sslmode": "disable"
    }
}