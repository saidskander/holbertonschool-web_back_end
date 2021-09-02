-- country rank origins
SELECT DISTINCT `origin`, SUM(`Fans`) as `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;
