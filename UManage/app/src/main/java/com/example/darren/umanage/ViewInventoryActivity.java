package com.example.darren.umanage;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
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
import java.util.Iterator;
import java.util.List;
import java.util.Map;

public class ViewInventoryActivity extends AppCompatActivity {

    ListView listView ;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_view_inventory);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        Intent receivedIntent = getIntent();
        String category = receivedIntent.getExtras().getString("category");

        Toast.makeText(getApplicationContext(), category, Toast.LENGTH_LONG).show();

        JSONObject request = new JSONObject();
        try {
            request.put("category", category);
        }catch(JSONException e){}

        RequestQueue queue = Volley.newRequestQueue(this);
        String url ="http://api.jdong.me/api/get_items";

        // Request a string response from the provided URL.
        JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.POST, url, request ,new Response.Listener<JSONObject>() {
            @Override
            public void onResponse(JSONObject response) {
                try {
                    ArrayList<String> displayList = new ArrayList<String>();
                    JSONObject resp = (JSONObject)response.get("items");
                    Iterator keys = resp.keys();
                    while(keys.hasNext()){
                        String key = (String)keys.next();       //item ID
                        String itemName = (String)resp.getJSONObject(key.toString()).get("name");
                        Integer count = (Integer)resp.getJSONObject(key.toString()).get("count");
                        displayList.add(itemName + " : " + count);

                    }
/*
                    JSONArray jsonArray = (JSONArray) response.get("items");
                    ArrayList<JSONObject> JSONObjectList = new ArrayList<JSONObject>();
                    if (jsonArray != null) {
                        int len = jsonArray.length();
                        for (int i=0;i<len;i++){
                            JSONObjectList.add((JSONObject)jsonArray.get(i));
                        }
                    }

                    Toast.makeText(getApplicationContext(), JSONObjectList.toString(), Toast.LENGTH_LONG).show();

                    //TODO: show count with item


                    listView = (ListView) findViewById(R.id.list);

                    ArrayList<String> displayList = new ArrayList<String>();

                    for(int i = 0; i < JSONObjectList.size(); i++){
                        String itemName = (String)JSONObjectList.get(i).get("item");
                        Integer count = (Integer)JSONObjectList.get(i).get("count");
                        displayList.add(itemName + " : " + count);
                    }
*/
                    listView = (ListView) findViewById(R.id.list);

                    ArrayAdapter<String> adapter = new ArrayAdapter<String>(ViewInventoryActivity.this,
                            android.R.layout.simple_list_item_1, android.R.id.text1, displayList);


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
    }

}
