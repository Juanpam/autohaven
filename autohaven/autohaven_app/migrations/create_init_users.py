# Generated by Django 5.0.6 on 2024-06-27 10:12

from django.db import migrations
from django.contrib.auth import get_user_model

def create_initial_users(apps, schema_editor):
    User = get_user_model()
    Group = apps.get_model('auth', 'Group')

    # Retrieve the group object by name

    group_name1 = "SuperUsers"  
    superuser_group = Group.objects.get(name=group_name1)
    

    group_name2 = "Sellers"  
    selleruser_group = Group.objects.get(name=group_name2)

    group_name3 = "RegularUsers"  
    regularuser_group = Group.objects.get(name=group_name3)


    # Create a superuser
    super_user, created = User.objects.get_or_create(
        username='superuser',
        defaults={
            'first_name': 'Super',
            'last_name': 'User',
            'email': 'superuser@gmail.com',
            'is_staff': True,
            'is_superuser': True
        }
    )
    if created:
        super_user.set_password('adminpassword')
        super_user.save()
        super_user.groups.add(superuser_group.id)

    # Create a seller user
    seller_user, created = User.objects.get_or_create(
        username='seller',
        defaults={
            'first_name': 'Seller',
            'last_name': 'User',
            'email': 'seller@icloud.com',
            'is_staff': False,
            'is_superuser': False
        }
    )
    if created:
        seller_user.set_password('sellerpassword')
        seller_user.save()
        seller_user.groups.add(selleruser_group.id)

    # Create a regular user
    regular_user, created = User.objects.get_or_create(
        username='regularuser',
        defaults={
            'first_name': 'Regular',
            'last_name': 'User',
            'email': 'regularuser@firefox.com',
            'is_staff': False,
            'is_superuser': False
        }
    )
    if created:
        regular_user.set_password('userpassword')
        regular_user.save()
        regular_user.groups.add(regularuser_group.id)



class Migration(migrations.Migration):

    dependencies = [
        ('autohaven_app', 'create_init_groups'),
    ]

    operations = [migrations.RunPython(create_initial_users),
    ]