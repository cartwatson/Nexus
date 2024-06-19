import os
import psycopg2


def main():
    conn = psycopg2.connect(
        host="localhost",
        dbname=os.environ['POSTGRES_DB'],
        user=os.environ['POSTGRES_USER'],
        password=os.environ['POSTGRES_PASSWORD'],
        port=os.environ['POSTGRES_PORT'],
    )

    cur = conn.cursor()

    # create table for satellites
    cur.execute(
        """CREATE TABLE IF NOT EXISTS satellites (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE,
        altitude NUMERIC(100),
        velocity NUMERIC(100)
        );
        """
    )

    # create table for droids
    cur.execute(
        """CREATE TABLE IF NOT EXISTS droids (
        id SMALLSERIAL PRIMARY KEY,
        name VARCHAR(255) UNIQUE
        );
        """
    )

    # init DROID satellite
    cur.execute(
        """INSERT INTO droids (name) VALUES
        ('DROID-001')
        """
    )

    # create table for images
    cur.execute(
        """CREATE TABLE IF NOT EXISTS images (
        id SERIAL PRIMARY KEY,
        time_taken TIMESTAMP,
        taken_by INT NOT NULL,
        id_sat INT NOT NULL,
        img bytea,
        CONSTRAINT fk_satellites
            FOREIGN KEY (id_sat)
            REFERENCES satellites(id),
        CONSTRAINT fk_droids
            FOREIGN KEY (taken_by)
            REFERENCES droids(id)
        );
        """
    )

    # create table for image-requests
    cur.execute(
        """CREATE TABLE IF NOT EXISTS requests (
        id SERIAL PRIMARY KEY,
        time TIMESTAMP,
        target_sat INT NOT NULL,
        pending BOOLEAN,
        fulfilled BOOLEAN,
        CONSTRAINT fk_satellites
            FOREIGN KEY (target_sat)
            REFERENCES satellites(id)
        );
        """
    )

    conn.commit()

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
