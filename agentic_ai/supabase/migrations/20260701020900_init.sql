create schema if not exists public;
create schema if not exists vector;

create extension if not exists vector with schema vector;

set search_path = public, vector;

create table public.documents (
    id uuid primary key default gen_random_uuid(),
    content text not null,
    metadata jsonb,
    vectors vector(1024)
);

grant usage on schema vector to anon, authenticated, service_role;
grant usage on schema public to anon, authenticated, service_role;
grant select, insert, update, delete on table public.documents to anon, authenticated, service_role;
