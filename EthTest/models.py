from django.db import models

# Create your models here.

class Blocks(models.Model):
    block_number= models.IntegerField(primary_key = True)
    block_hash  = models.CharField(max_length=100)
    timestamp   = models.CharField(max_length=100)
    prev_block_hash = models.CharField(max_length=100)
    nonce       = models.CharField(max_length=100)
    miner_addr  = models.CharField(max_length=100)
    difficulty  = models.CharField(max_length=100)
    size_bytes  = models.IntegerField()
    extra_data  = models.CharField(max_length=3000)

class Transactions(models.Model):
    block_number = models.IntegerField()
    block_hash   = models.CharField(max_length=100)
    tx_from      = models.CharField(max_length=100)
    tx_hash      = models.CharField(max_length=100,primary_key = True)
    tx_index     = models.CharField(max_length=100)
    tx_input     = models.CharField(max_length=10000)
    tx_value     = models.CharField(max_length=100)
    tx_type      = models.IntegerField()
    nonce        = models.IntegerField()
    tx_to        = models.CharField(max_length=100)

class number_tx_in_block(models.Model):
    block_number = models.IntegerField(primary_key = True)
    number       = models.IntegerField()

class Tx_Block(models.Model):
    tx_hash     = models.CharField(max_length=100)
    block_number= models.IntegerField()
    block_hash  = models.CharField(max_length=100)



