f you’re enchanted by timeless love stories, you would have appreciated our tale of discovery and resolution. Join us as we delved into the recent outage that affected our e-commerce website's login service, drawing parallels with the tragic romance of Romeo and Juliet.

On June 1, 2023, between 10:00 AM and 11:30 AM EST, the login service of our e-commerce website was down, affecting 60% of our users. Users attempting to log in were met with an error message, unable to access their accounts or complete purchases.

Much like the star-crossed lovers, we faced an unexpected and challenging situation. Fortunately, the issue was resolved by reversing a recent software deployment and restarting the web server. Our story didn’t end there; we implemented a series of corrective and preventative measures to ensure this wouldn’t happen again. If you were intrigued by the drama and resolution of classic tales, or just wanted to know how we resolved our recent outage, come along for the ride!

Timeline:

10:00 AM EST: The issue was detected when our monitoring system reported a sudden spike in error rates for the login service.
10:02 AM EST: The engineering team was alerted and began investigating the issue.
10:05 AM EST: The team discovered that the login service was not responding to requests and attempted to restart the service.
10:10 AM EST: Restarting the service did not resolve the issue, prompting further investigation into a possible software deployment problem.
10:15 AM EST: The team noticed abnormal memory usage on the web server and suspected it was the root cause.
10:20 AM EST: Attempts to free up memory and optimize server performance did not yield significant improvements.
10:30 AM EST: The incident was escalated to the senior engineering team and server administrators.
10:35 AM EST: Server administrators identified a recent software deployment that caused a memory leak, preventing the login service from functioning properly.
10:40 AM EST: The deployment was rolled back, and the web server was restarted.
11:00 AM EST: The login service was restored, allowing users to log in and complete purchases.
11:30 AM EST: The incident was declared resolved.
Root Cause and Resolution:

The root cause of the outage was a recent software deployment that introduced a memory leak, causing the login service to malfunction. The issue was resolved by reversing the deployment and restarting the web server.

Corrective and Preventative Measures:

To prevent similar incidents in the future, we implemented the following measures:

Improved Monitoring: Enhanced monitoring of server performance metrics to detect issues earlier.
Reviewed and Tested Deployments: Thoroughly reviewed and tested software deployments before releasing them to production.
Documentation and Training: Improved documentation and training for developers to ensure proper deployment management.
System Redundancy: Added more redundancy and failover mechanisms to the login service to minimize the impact of similar incidents.
Memory Optimization: Reviewed server configurations and memory management practices to identify and address potential performance bottlenecks.
