package com.example.darren.umanage;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.Toast;

public class MainMenuActivity extends AppCompatActivity {

    String category;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_menu);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        Intent receivedIntent = getIntent();
        category = receivedIntent.getExtras().getString("category");

        Toast.makeText(getApplicationContext(), category, Toast.LENGTH_LONG).show();
    }

    public void addToInventory(View view){
        Intent intent = new Intent(this, BarcodeScannerActivity.class);
        intent.putExtra("category", category);
        intent.putExtra("edit_choice", "add");
        startActivity(intent);
    }

    public void removeFromInventory(View view){
        Intent intent = new Intent(this, BarcodeScannerActivity.class);
        intent.putExtra("category", category);
        intent.putExtra("edit_choice", "remove");
        startActivity(intent);
    }

    public void viewInventory(View view){
        Intent intent = new Intent(this, ViewInventoryActivity.class);
        intent.putExtra("category", category);
        startActivity(intent);
    }

    public void switchInventory(View view){
        Intent intent = new Intent(this, InventorySelectActivity.class);
        startActivity(intent);
    }

}
