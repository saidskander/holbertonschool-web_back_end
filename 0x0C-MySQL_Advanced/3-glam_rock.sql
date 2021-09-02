-- lists all bands
SELECT DISTINCT band_name, (IFNULL(`split`, 2021) - formed) AS lifespan FROM metal_bands WHERE style LIKE 'Glam rock' ORDER BY lifespan DESC;
