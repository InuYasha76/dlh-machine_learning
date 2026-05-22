// List MongoDB Databases, format: | Name padded | Size 3 decimal places+GB) |
var jsonJSObject = db.adminCommand({ listDatabases: 1 });
var listDatabases = jsonJSObject.databases;
listDatabases.forEach(d => {
	var paddedName = d.name.padEnd(13, " ");
	var dbSize = d.sizeOnDisk / (1024 ** 3);
	dbSize = dbSize.toFixed(3) + "GB";
	print(paddedName + dbSize);
});
