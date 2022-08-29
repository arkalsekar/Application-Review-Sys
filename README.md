# Application Review System (ARS)

This is a complete Application Review System made using Django and Boostrap. It has all the features required for an ARS. 

## Demo 
![Demo 1](https://github.com/arkalsekar/application-review-sys/blob/main/static/demo1.JPG?raw=true)


## Characteristics

Here are the Features of the Application created.
</br>
1. Complete User Authentication and Autherization using Django
2. Each User can only Fill Application once
3. He can Later Track his Application via provided Application ID
4. Status Will be Shown whether his Application has been acccepted or rejected by the Admin. 

## Setting Up

Clone or Download the this repository and store it on your machine. 
```bash
git clone https://github.com/arkalsekar/application-review-sys/
```

## Usage
Once Downloaded or Cloned the Repository, Run the following Commands

```bash
pip install -r requirements.txt
```
Once Installed all the requirements. Run the Following Commands.
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
This is isin't necessary but with this you would be able to login to the website.
```bash
python manage.py createsuperuser
```
This command will finally run the server on localhost://8000
```bash
python manage.py runserver
```
Now head on to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and access the site.


## License
[MIT](https://choosealicense.com/licenses/mit/)
