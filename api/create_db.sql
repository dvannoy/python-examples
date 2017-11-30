drop table if exists vehicle_stops;
create table vehicle_stops (
    stop_id String, stop_cause String, service_area String, subject_race String,
     subject_sex String, subject_age String, timestamp String, stop_date String,
     stop_time String, sd_resident String, arrested String, searched String,
     obtained_consent String, contraband_found String, property_seized String
);

.separator ","
.import /data1/tmp/vehicle_stops_2016_datasd_clean.csv vehicle_stops