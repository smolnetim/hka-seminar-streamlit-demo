CREATE DATABASE streamlit_web WITH template = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_US.UTF-8';
ALTER DATABASE streamlit_web OWNER TO streamlit;

\c streamlit_web;

CREATE TABLE "public"."dataset" (
    "created_at" timestamptz NOT NULL DEFAULT now(),
    "value1" integer NOT NULL,
    "value2" integer NOT NULL, PRIMARY KEY ("created_at")
);

CREATE OR REPLACE FUNCTION insert_dataset_entries()
RETURNS VOID AS $$
DECLARE
    i integer;
    last_value1 integer;
    last_value2 integer;
    time_stamp timestamp := '2023-01-01 00:00:00';
BEGIN
    -- Initialize last_value1 and last_value2 with a random value between 0 and 500
    last_value1 := floor(random() * 500)::integer;
    last_value2 := floor(random() * 500)::integer;

    -- Insert 2880 entries
    FOR i IN 1..2880 LOOP
        -- Insert a new row
        INSERT INTO public.dataset(created_at, value1, value2)
        VALUES (time_stamp, last_value1, last_value2);

        -- Update time_stamp, last_value1 and last_value2 for the next iteration
        time_stamp := time_stamp + interval '30 seconds';
        last_value1 := last_value1 + floor(random() * 21 - 10)::integer;
        last_value2 := last_value2 + floor(random() * 21 - 10)::integer;

        -- Make sure last_value1 and last_value2 stay between 0 and 500
        IF last_value1 < 0 THEN
            last_value1 := 0;
        ELSIF last_value1 > 500 THEN
            last_value1 := 500;
        END IF;

        IF last_value2 < 0 THEN
            last_value2 := 0;
        ELSIF last_value2 > 500 THEN
            last_value2 := 500;
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

SELECT insert_dataset_entries();
