from django.db import migrations


def seed(apps, schema_editor):
    Fad = apps.get_model('nostaldja_sub', 'Fad')
    Decade = apps.get_model('nostaldja_sub', 'Decade')
    eighties = Decade(start_year="1980s")
    nineties = Decade(start_year="1990s")
    oughts = Decade(start_year="2000s")
    tens = Decade(start_year="2010s")
    eighties.save()
    nineties.save()
    oughts.save()
    tens.save()

    Fad(decade=tens, name='Fidget Spinners', description='A fidget spinner is a toy that consists of a ball bearing in the center of a multi-lobed (typically two or three) flat structure made from metal or plastic designed to spin along its axis with little effort. Fidget spinners became popular toys in April 2017, although similar devices had been invented as early as 1993. ',
        image_url='https://www.dhresource.com/0x0s/f2-albu-g5-M01-79-07-rBVaJFiuqDSAF3I7AAKBk1FyKy0267.jpg/hand-spinner-fidget-spinner-tri-spinner-diy.jpg').save()
    Fad(decade=tens, name='Block Chain', description='A blockchain, originally block chain, is a continuously growing list of records, called blocks, which are linked and secured using cryptography. Each block typically contains a cryptographic hash of the previous block, a timestamp and transaction data. By design, a blockchain is inherently resistant to modification of the data.',
        image_url='https://blogs.iadb.org/caribbean-dev-trends/wp-content/uploads/sites/34/2017/12/Blockchain1.jpg').save()
    Fad(decade=oughts, name='Silly Bandz', description='Silly Bandz are rubber bands made of silicone rubber formed into shapes including animals, objects, numbers, and letters. ',
        image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Silly_Bandz_2009.jpg/2560px-Silly_Bandz_2009.jpg').save()
    Fad(decade=oughts, name='iPods', description='iPhone - Phone = iPod',
        image_url='https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/ipod-touch-select-blue-2019_GEO_US_FMT_WHH?wid=940&hei=1112&fmt=png-alpha&.v=1558124595488').save()
    Fad(decade=oughts, name='Myspace', description='Myspace (stylized as MySpace) is a social networking website offering an interactive, user-submitted network of friends, personal profiles, blogs, groups, photos, music, and videos. Myspace was the largest social networking site in the world, from 2004 to 2010.',
        image_url='https://us.hellomagazine.com/imagenes/travel/2018012645793/tom-myspace-founder-travel-photographer/0-230-700/myspace-tom-now-t.jpg').save()
    Fad(decade=nineties, name='JNCOs', description='JNCO, short for "Judge None Choose One", is a Los Angeles, California based clothing company specializing in boys\' and men\'s jeans.',
        image_url='http://cdn.shopify.com/s/files/1/0022/0446/7300/products/2021.08.16_Jnco0754_grande.jpg?v=1629831679').save()


def fallow(apps, schema_editor):
    Fad = apps.get_model('nostaldja_sub', 'Fad')
    Decade = apps.get_model('nostaldja_sub', 'Decade')
    Decade.objects.all().delete()
    Fad.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('nostaldja_sub', '0002_alter_decade_start_year'),
    ]

    operations = [
        migrations.RunPython(seed, fallow)
    ]
