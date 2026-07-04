alter table public.chats
    drop column messages, 
    add column state jsonb not null;