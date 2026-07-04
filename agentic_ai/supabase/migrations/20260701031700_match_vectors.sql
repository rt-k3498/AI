create or replace function public.match_vectors(
    query_vector vector.vector(1024),
    top_k int, 
    similarity_threshold float8
) returns setof documents
language sql 
set search_path = public, vector
as $$
    select * from documents
    where vectors <=> query_vector < (1 - similarity_threshold)
    order by vectors <=> query_vector asc
    limit top_k;
$$;

create role user123 login password 'test123';
grant authenticated to user123;
