package com.example.darren.umanage;

import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;
import com.google.zxing.integration.android.IntentIntegrator;
import com.google.zxing.integration.android.IntentResult;

import org.json.JSONObject;

public class BarcodeScannerActivity extends AppCompatActivity {

    private TextView formatTxt, contentTxt;
    String category, edit_choice;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_barcode_scanner);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);

        Intent receivedIntent = getIntent();
        category = receivedIntent.getExtras().getString("category");
        edit_choice = receivedIntent.getExtras().getString("edit_choice");

        formatTxt = (TextView) findViewById(R.id.scan_format);
        contentTxt = (TextView) findViewById(R.id.scan_content);
    }

    public void scan(View view) {
        IntentIntegrator integrator = new IntentIntegrator(this);
        if (edit_choice.equals("add")) {
            integrator.setPrompt("ADD ITEM");
        } else {
            integrator.setPrompt("REMOVE ITEM");
        }
        integrator.initiateScan();
    }

    public void onActivityResult(int requestCode, int resultCode, Intent intent) {
        IntentResult scanningResult = IntentIntegrator.parseActivityResult(requestCode, resultCode, intent);
        if (scanningResult != null) {
            String scanContent = scanningResult.getContents();
            String scanFormat = scanningResult.getFormatName();
            formatTxt.setText("FORMAT: " + scanFormat);
            contentTxt.setText("CONTENT: " + scanContent);

            RequestQueue queue = Volley.newRequestQueue(this);
            String url = "http://api.jdong.me/api/add_item";
            JSONObject request = new JSONObject();
            try {
                if (edit_choice.equals("add")) {
                    request.put("category", category);
                    request.put("item_id", scanContent);
                    request.put("count", 1);
                } else if (edit_choice.equals("remove")) {
                    request.put("category", category);
                    request.put("item_id", scanContent);
                    request.put("count", -1);
                }
            } catch (Exception e) {
                Toast.makeText(getApplicationContext(), "Exception caught", Toast.LENGTH_LONG).show();
            }

            // Request a string response from the provided URL.
            JsonObjectRequest stringRequest = new JsonObjectRequest(Request.Method.POST, url, request, new Response.Listener<JSONObject>() {
                @Override
                public void onResponse(JSONObject responseObj) {
                    try {
                        String receivedAction = responseObj.getString("action");
                        String receivedStatus = responseObj.getString("status");
                        Toast.makeText(getApplicationContext(), receivedAction + " " + receivedStatus, Toast.LENGTH_LONG).show();
                    } catch (Exception e) {
                        Toast.makeText(getApplicationContext(), "onResponse(): Exception caught", Toast.LENGTH_LONG).show();
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
}
