package com.example.darren.umanage;

/**
 * Created by Darren on 4/29/2016.
 */
public class Item {
    String itemName;
    int count;

    public Item(String itemName){
        this.itemName = itemName;
        count = 0;
    }

    public Item(String itemName, int count){
        this.itemName = itemName;
        this.count = count;
    }

    public int getCount(){
        return this.count;
    }

    public void setCount(int newCount){
        this.count = newCount;
    }

    public String getName(){
        return this.itemName;
    }

    public void setName(String newName){
        this.itemName = newName;
    }
}
