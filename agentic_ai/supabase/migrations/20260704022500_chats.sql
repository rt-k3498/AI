create table public.chats (
    id uuid primary key default uuid_generate_v4(),
    messages jsonb not null
);

grant select, insert, update, delete on public.chats to authenticated, postgres;