# pynetloc
Yet another expanded-pythonnet module.

This is about wrapping C# Geolocation services to provide easy pythonic access to Window's Geolocation services.
    
Additionally some convience functions are provided, for instance the `GeoCoordinateWatcher` has a `location` property
    which is the same as getting the `position.location` property.

**WARNING**: This only works if C#'s GeoCoordinateWatcher works, which only works if Window's location services are turned on.
    If they are not, you may get a NoData status and an unknown position.

### Example
The basics are the same as C#'s GeoCoordinateWatcher, but with the added benefits of expanded-pythonnet.

First the watcher needs to be spawned and started. Then we can start pulling data, if there is data.
```pydocstring
>>> from netloc import GeoCoordinateWatcher, GeoPositionStatus
>>> watcher = GeoCoordinateWatcher()
>>> watcher.try_start(suppress_permission_prompt=False)
True
>>> watcher.status == GeoPositionStatus.Ready
True
>>> watcher.location.is_unknown
False
>>> (watcher.location.latitude, watcher.location.longitude)
(38.89738554927472, -77.03750976566602)
```