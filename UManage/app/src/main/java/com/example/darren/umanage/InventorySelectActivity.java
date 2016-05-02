package com.example.darren.umanage;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;

public class InventorySelectActivity extends AppCompatActivity {

    ListView listView ;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_inventory_select);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        RequestQueue queue = Volley.newRequestQueue(this);
        String url ="http://api.jdong.me/api/get_categories";

        // Request a string response from the provided URL.
        JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.GET, url, null ,new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                try {
                    JSONArray jsonArray = (JSONArray) response.get("categories");
                    ArrayList<String> list = new ArrayList<String>();
                    if (jsonArray != null) {
                        int len = jsonArray.length();
                        for (int i=0;i<len;i++){
                            list.add(jsonArray.get(i).toString());
                        }
                    }

                    Toast.makeText(getApplicationContext(), list.toString(), Toast.LENGTH_LONG).show();

                    listView = (ListView) findViewById(R.id.list);

                    ArrayAdapter<String> adapter = new ArrayAdapter<String>(InventorySelectActivity.this,
                            android.R.layout.simple_list_item_1, android.R.id.text1, list);


                    // Assign adapter to ListView
                    listView.setAdapter(adapter);

                    // ListView Item Click Listener
                    listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {

                        @Override
                        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                            String itemValue = (String) listView.getItemAtPosition(position);

                            Intent intent = new Intent(InventorySelectActivity.this, MainMenuActivity.class);
                            intent.putExtra("category", itemValue);
                            startActivity(intent);
                        }

                    });
                }catch(JSONException e){
                    Toast.makeText(getApplicationContext(), "Exception caught", Toast.LENGTH_LONG).show();
                }
            }
        }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                Toast.makeText(getApplicationContext(), "Error", Toast.LENGTH_LONG).show();
            }
        });
        // Add the request to the RequestQueue.
        queue.add(stringRequest);

        /*

        // Get ListView object from xml
        listView = (ListView) findViewById(R.id.list);

        // Defined Array values to show in ListView
        //TODO: Pull list from server
        String[] values = new String[] {
                "Inventory1",
                "Inventory2",
                "Inventory3",
                "Inventory4"
        };

        // Define a new Adapter
        // First parameter - Context
        // Second parameter - Layout for the row
        // Third parameter - ID of the TextView to which the data is written
        // Forth - the Array of data

        ArrayAdapter<String> adapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1, android.R.id.text1, values);


        // Assign adapter to ListView
        listView.setAdapter(adapter);

        // ListView Item Click Listener
        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {

            @Override
            public void onItemClick(AdapterView<?> parent, View view, int position, long id) {

                // ListView Clicked item index
                int itemPosition = position;

                // ListView Clicked item value
                String itemValue = (String) listView.getItemAtPosition(position);

                // Show Alert
                Toast.makeText(getApplicationContext(),
                        "Position :" + itemPosition + "  ListItem : " + itemValue, Toast.LENGTH_LONG)
                        .show();

                //switch to main menu activity
                Intent intent = new Intent(InventorySelectActivity.this, MainMenuActivity.class);
                startActivity(intent);

            }

        });
        */
    }
}
