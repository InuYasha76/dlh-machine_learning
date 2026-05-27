-- Create an index on the 'names' tab.
-- Only the first letter of name is indexed.

CREATE INDEX idx_name_first ON names (name(1));
