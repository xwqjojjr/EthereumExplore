from EthTest.models import Blocks,Tx_Block,number_tx_in_block
from django.shortcuts import render, HttpResponse, redirect
# Create your views here.

def index(request):
    return render(request,'EthTest/test.html')

def ShowBlocks(request):
    blocks = Blocks.objects.all()
    return render(request, 'EthTest/ShowBlocks.html', {'Blocks': blocks})

def Show_number_tx_in_block(request):
    # insert into EthTest_number_tx_in_block(number,block_number) select count(*),block_number from EthTest_tx_block group by block_number;
    tx_block = number_tx_in_block.objects.all()
    listx = []
    listy = []
    for tb in tx_block:
        listx.append(int(tb.block_number))
        listy.append(int(tb.number))
    number   = number_tx_in_block.objects.values("number")
    block_number = number_tx_in_block.objects.values("block_number")
    return render(request, 'EthTest/ShowNumberTxInBlock.html', {'Tx_Block':tx_block,'Number':number,'Block_Number':block_number,'X':listx, 'Y':listy})