# ProctorTab

This XBlock is used to add new tab to course detail page. Once user clicks on "Proctortrack" tab, it will load https://www.proctortrack.com/ as a tab detail

#### Support version: Ironwood

#### Installation Steps for development
1. Go to your devstack directory where we can access our `make` commands and execute bellow commands.
    ```sh
    $ make lms-shell
    $ source /edx/app/edxapp/edxapp_env
    $ pip install -e git+https://github.com/khushu729/proctortrack-tab.git@master#egg=proctortrack-tab
    $ sudo chown -R edxapp:edxapp /edx/app/edxapp/venvs/edxapp/src/proctortrack-tab/
    ```
2. Execute above commands to studio-shell.
    ```sh
    $ make lms-shell
    $ source /edx/app/edxapp/edxapp_env
    $ pip install -e git+https://github.com/khushu729/proctortrack-tab.git@master#egg=proctortrack-tab
    $ sudo chown -R edxapp:edxapp /edx/app/edxapp/venvs/edxapp/src/proctortrack-tab/
    ```
3. Add xblock name in `lms.env.json` 
    `ADDL_INSTALLED_APPS`: `["proctortrack_tab"],`

4. Add in `lms/urls.py` before `static_tab` url.
    ```sh
    urlpatterns += [
        url(
          r'^courses/{}/proctortrack/'.format(
              settings.COURSE_ID_PATTERN,
          ),
          include('proctortrack_tab.urls'),
        )
    ],
    ```
5. Restart lms and studio server.
    ```sh
    $ make lms-restart && make studio-restart
    ```
#### Installation For production environments...
1. Login to edxapp user
    ```sh
    $ sudo -Hs -u edxapp bash
    ```
2. Activate edxapp_env
3. Install proctortrack_tab xblock.
    ```sh
    $ pip install -e git+https://github.com/khushu729/proctortrack-tab.git@master#egg=proctortrack-tab
    ```

4. Add xblock name in `lms.env.json` 
    `ADDL_INSTALLED_APPS`: `["proctortrack_tab"],`

5. Add in `lms/urls.py` before `static_tab` url.
    ```sh
    urlpatterns += [
        url(
          r'^courses/{}/proctortrack/'.format(
              settings.COURSE_ID_PATTERN,
          ),
          include('proctortrack_tab.urls'),
        )
    ],
    ```
6. Restart lms and studio server.
    ```sh
    $ sudo /edx/bin/supervisorctl restart cms lms
    ```
    
#### Note:
* The course stores a static list of its tabs in the database, and this list is only updated when one of the following actions take place:
    1. You create a new course.
    2. You update the advanced settings for your course.
* This means that if you have a pre-existing course then it won't immediately show a tab even after you've registered the new entry point

#### Second Option to add Tab:
We can also add a tab to specific course from studio.
1. Open Studio with instructor credential and select course in which you want to add a custom tab
2. Select option from menu. `Content` > `Pages` > `Add New Page`.
3. `Edit` tab name and content as per our requirements and `save` changes.
