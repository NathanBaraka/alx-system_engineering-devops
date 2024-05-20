<<<<<<< HEAD
## MySQL primary replica setup

A primary-replica cluster, also known as master-slave replication, is a setup in MySQL where one server acts as the primary (master) and one or more servers act as replicas (slaves). The primary server receives write operations (inserts, updates, deletes), and these changes are then replicated to the replica servers, ensuring data consistency and fault tolerance.

## Build a robust database backup strategy

A robust database backup strategy is essential for ensuring data integrity and disaster recovery. It involves regularly backing up the database to prevent data loss in case of hardware failure, human error, or other disasters. Key aspects of a backup strategy include determining backup frequency, choosing appropriate backup methods (full, incremental, or differential backups), storing backups securely, and regularly testing the backup and restore process to ensure reliability.

## MySQL primary replica setup

A MySQL primary replica setup involves configuring one MySQL server as the primary server (master) and one or more servers as replica servers (slaves). The primary server receives write operations (inserts, updates, deletes) from applications, and these changes are then replicated to the replica servers. This setup provides fault tolerance, load distribution, and read scalability.
=======
## What is the main role of a database?

The main role of a database is to store, organize, and manage data in a structured format. It provides mechanisms for storing, retrieving, updating, and deleting data, allowing users and applications to access and manipulate information efficiently.

## What is a database replica?

A database replica is an exact copy of a database that is synchronized with the original database. It serves as a backup or standby database that can be used for failover, disaster recovery, read scaling, or other purposes. Changes made to the original database are replicated to the replica database, ensuring data consistency between the two.

## What is the purpose of a database replica?

The purpose of a database replica is to provide redundancy, fault tolerance, and scalability for database systems. By maintaining one or more replicas of the original database, organizations can minimize downtime, improve performance, and enhance data availability in case of hardware failures, software errors, or other disruptions.

## Why do database backups need to be stored in different physical locations?

Database backups need to be stored in different physical locations to protect against data loss due to disasters such as fires, floods, earthquakes, or theft. Storing backups in multiple locations reduces the risk of losing all backup copies simultaneously and ensures that data can be recovered even if one location becomes inaccessible.

## What operation should you regularly perform to make sure that your database backup strategy actually works?

To ensure that your database backup strategy works effectively, you should regularly perform backup testing and validation. This involves simulating backup and restore scenarios to verify that backups are being created correctly, can be restored successfully, and that the restored data is consistent and usable. Regular testing helps identify any issues or weaknesses in the backup process and allows you to address them proactively.
>>>>>>> 421d8eb972349f295f9f97b83f9d21b132b5f1a6

