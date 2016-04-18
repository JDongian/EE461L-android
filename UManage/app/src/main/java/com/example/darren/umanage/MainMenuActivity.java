package com.example.darren.umanage;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;

public class MainMenuActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_menu);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
    }

    public void addToInventory(View view){
        Intent intent = new Intent(this, BarcodeScannerActivity.class);
        startActivity(intent);
    }

    public void removeFromInventory(View view){
        Intent intent = new Intent(this, BarcodeScannerActivity.class);
        startActivity(intent);
    }

    public void viewInventory(View view){
        Intent intent = new Intent(this, ViewInventoryActivity.class);
        startActivity(intent);
    }

    public void switchInventory(View view){
        Intent intent = new Intent(this, InventorySelectActivity.class);
        startActivity(intent);
    }

}
