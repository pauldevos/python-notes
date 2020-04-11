### Deploying Python Web Apps - Python Dashboards
The candidates are:
- Bokeh Server
- Jupyter Server
- Panel
- Plotly


### Dash vs Panel
- Dash dashboards store all of their per-user session state in the client (i.e., the browser), while Panel allows per-user, per-session state in both the server and the client, synchronizing between the two if needed. This difference has important implications:

- Dash’s approach is more highly scalable in some cases, allowing many simultaneous client sessions without necessarily using up resources on the server for each new client.

- Dash’s approach requires dashboards to be written only in a reactive way, with logic defined by Python callback functions that have no side effects; imperative functions that change Python-based state are not supported. 
- Panel supports server-side caching of intermediate results and other state per user, which can make complex processing pipelines that need server-side data much more practical. For instance, both approaches can generate and update Datashader plots as a user pans and zooms, using large datasets stored only on the server, but they will work in very different ways. With Dash, all requests will need to start with the original dataset and do all the processing steps needed to fill a client request, returning the final plot rendered for the client to show, because no intermediate data will be stored on the server for a subsequent call to use. With Panel, it is possible to write apps that re-run only the very specific computations needed for a specific request, making use of previously computed intermediate values stored per user and per session on the server and never communicated to the client. The [Datashader example dashboard](https://examples.pyviz.org/datashader_dashboard/dashboard.html) shows how to use this intermediate-value caching to provide the fastest possible updates for a given user action, only re-running the computation actually needed to satisfy the request, re-using cached values stored on the server when appropriate.

### Voila vs Bokeh
- If you don’t need ipywidget support, you can use either Bokeh Server or Voila for serving Panel objects. Which one should you choose? Both servers are based on Tornado under the hood, but they differ in the fact that Jupyter will launch a new Python kernel for each user, while the Bokeh server can serve multiple users on the same process. This subtle difference has two major implications:
- The per-user overhead for a Bokeh app is much lower. Once the relevant libraries are imported, there is only a tiny bit of overhead for creating each new session. The Jupyter server, on the other hand, always launches an entirely new process, with all the overhead that entails. For a session that imports nothing but pandas and matplotlib the per-user overhead is 75 MB (as of 10/2019), which increases for more complex environments.
- Since a Bokeh server shares a single process for multiple sessions, data or processing can also be shared between the different sessions where appropriate. Such sharing makes it possible to further reduce the memory footprint of a Bokeh-Server app, to make it practical to support larger numbers of users and to provide faster startup or data-access times.



Sources:
- [](https://panel.holoviz.org/Comparisons.html)