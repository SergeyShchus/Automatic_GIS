- Written in Python, these routines can run on any OS that supports Python, ArcGIS, and ArcPy.
- Using the ALF-Lite architecture will reduce the demand on Enterprise Resources by leveraging the File Geodatabase.
- Lightweight and simple enough to run on a single User's Desktop, yet powerful enough to scale out to a distributed, multi-tiered environment. Use your Python skills and tailor to your needs!
- The 'Log' files are automatically maintained by the Logger object found in the ALFlib library.
- The 'Deployment' logic is integrated into a user-maintained configuration file. It's up to you how to deploy the data. By default, the Feed Routines copy their workspace to a Live folder, ready for consumption.
- The 'Live' FileGDB can be directly consumed by ArcGIS Desktop or published by ArcGIS Server using a Map Service even while the script updates the underlying data. Eliminating the need to re-cycle live services just to refresh a data source!
- To maintain the Live data on a regular interval, schedule a task or cron job to run the Feed Routine as often as needed to keep the data current.
Here's an example map of live Rain fall intensity (precipitation), NOAA Weather Advisories, and Wind Speed and Direction data all prepared by ALF-Lite routines and published using ArcGIS Server Map Services:
