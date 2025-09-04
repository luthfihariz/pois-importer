# Take Home Exercise

Thank you for speaking with Hess and for taking the time to engage in the recruitment process with us. As she mentioned, the next stage of our hiring process is a take home exercise (below) which is designed to give us a better picture of your skills, thought process and working habits as a software engineer in a production environment.

The exercise should take around 2 hours. If the project isn't complete by then, please ensure you leave a list "what you didn't have time to complete" so that when the team assess it, they have more context.

If you have any questions or concerns, please feel free to contact us.

## Background

SearchSmartly needs to process data from many different sources. There are text files that we fetch from different places and we then import the contents of each file into our database.

There are lots of different types of files but, for this project, we are only concerned with the 3 file types (CSV, JSON and XML) that contain Point of Interest (PoI) data.

We need a new service that can import these files and allow their information to be browsed via the web via the Django Admin Panel. For this challenge, files will be imported via the command-line.

## Requirements

### Submission Process

When you have completed the task, please share it back to us via a git repository. The repo should contain at least a Django web application (see below for application requirements) with a README.md that explains how to install and use the project.

Feel free to document any assumptions that you have made, along with ideas for improving the project.

### Application Requirements

1. The application should be a Django project that runs on Python 3.10 or above.

2. It should have a management command that can be called with the path to a file (or files). The relevant data for each PoI should be extracted and stored in a local database.

3. The specification for these files is included in the application notes below. You will also find a link to each file in that section.

4. There should also be a Django admin site that display the following data:
   - PoI internal ID
   - PoI name
   - PoI external ID
   - PoI category
   - Avg. rating

5. In addition, the application should permit a user to search for the values associated with either:
   - PoI internal ID
   - PoI external ID

6. And finally, there should be a filter by category.

## Application Notes

The models and database schema are up to you. Don't worry about deployment to a remote environment - concentrate on ensuring the project works locally.

### Files Specification

- **CSV**: `poi_id`, `poi_name`, `poi_latitude`, `poi_longitude`, `poi_category`, `poi_ratings`
- **JSON**: `id`, `name`, `coordinates[latitude, longitude]`, `category`, `ratings`, `description`
- **XML**: `pid`, `pname`, `platitude`, `plongitude`, `pcategory`, `pratings`