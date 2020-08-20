-------------------------------------- TEXT PLUGIN -------------------------

-- Insert Plugin
insert into plugin (qualified_library_name, description) values( '/usr/local/lib/libText_Plugin.so', 'This is a plugin that extracts Text information from Text file' );

-- Insert tag sets
insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 1, 1, 'Text.Text', 'Text from text file');

-------------------------------------- FILETYPE PLUGIN -------------------------

-- Insert Plugin
insert into plugin (qualified_library_name, description) values( '/usr/local/lib/libFileType_Plugin.so', 'This is a plugin that stores the file type' );

-- Insert tag sets
insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 1, 1, 'FileType', 'Type of file');

-------------------------------------- COLOR PlUGIN -------------------------

insert into plugin (qualified_library_name, description) values( '/usr/local/lib/libColor_Plugin.so', 'This is a plugin that calculates average rgb values for images.' );

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Average.Red', 'Average Red');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Average.Blue', 'Average Blue');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Average.Green', 'Average Green');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 5, 5, 'RGB', 'RGB');

-------------------------------------- EXIF PLUGIN -------------------------

-- Insert Plugin
insert into plugin (qualified_library_name, description) values( '/usr/local/lib/libEXIF_Plugin.so', 'This is a plugin that extracts EXIF information from photographs' );

-- Insert tag sets
insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 1, 1, 'Exif.Image.Make', 'Camera manufacturer');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 1, 1, 'Exif.Image.Model', 'Camera model');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 1, 1, 'Exif.Image.Artist', 'Image artist');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 1, 1, 'Exif.Image.Software', 'Processing software');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 3, 3, 'Exif.Image.DateTime - DATE', 'Image creation date');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 4, 4, 'Exif.Image.DateTime - TIME', 'Image creation time');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Exif.Photo.ExposureTime', 'Exposure time (sec)');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Exif.Photo.FNumber', 'F-Number');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Exif.Photo.ISOSpeedRatings', 'ISO Speed rating');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 3, 3, 'Exif.Photo.DateTimeOriginal - DATE', 'Photograph taken - Date');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 4, 4, 'Exif.Photo.DateTimeOriginal - TIME', 'Photograph taken - Time');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Exif.Photo.ShutterSpeedValue', 'Shutter speed');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Exif.Photo.ApertureValue', 'Aperture value');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Exif.Photo.FocalLength', 'Focal length (mm)');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Exif.Photo.PixelXDimension', 'X-Axis pixel dimension');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Exif.Photo.PixelYDimension', 'Y-Axis pixel dimension');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Exif.Iop.RelatedImageWidth', 'Original image X-Axis pixel dimension');

insert into plugin_tag_set (plugin_id, tag_set_type_id, tag_type_id, name, tag_set_name) values
( (select max(id) from plugin), 2, 2, 'Exif.Iop.RelatedImageLength', 'Original image Y-Axis pixel dimension');

