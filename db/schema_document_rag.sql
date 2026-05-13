-- Re-run safely during development (drops existing tables).
DROP TABLE IF EXISTS document_chunk CASCADE;
DROP TABLE IF EXISTS document CASCADE;

CREATE TABLE document (
    id   bigserial PRIMARY KEY,
    path text NOT NULL
);

CREATE TABLE document_chunk (
    id          bigserial PRIMARY KEY,
    content     text NOT NULL,
    embedding   vector(768),
    metadata    jsonb NOT NULL DEFAULT '{}'::jsonb,
    document_id bigint NOT NULL REFERENCES document (id) ON DELETE CASCADE
);

CREATE INDEX document_chunk_document_id_idx ON document_chunk (document_id);
