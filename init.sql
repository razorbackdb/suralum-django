alter session set "_ORACLE_SCRIPT"=true;
create user wingesfe identified by wingesfe; 
grant connect, create session, imp_full_database to wingesfe;
grant unlimited tablespace to wingesfe; 