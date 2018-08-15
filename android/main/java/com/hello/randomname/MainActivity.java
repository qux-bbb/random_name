package com.hello.randomname;

import android.content.res.AssetManager;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ScrollView;
import android.widget.TextView;

import java.io.InputStream;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    ScrollView scrollView;
    TextView nameListTextView;
    TextView lastNameTextView;
    Button generateNameButton;

    int nameNum = 0;
    List<String> generatedNames = new ArrayList<String>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        scrollView = findViewById(R.id.scrollView);
        nameListTextView = findViewById(R.id.name_list);
        lastNameTextView = findViewById(R.id.last_name);
        generateNameButton = findViewById(R.id.generate_button);

        nameListTextView.setTextIsSelectable(true);
        lastNameTextView.setTextIsSelectable(true);

        final String[] xings = getWords("xing.txt");
        final String[] mings = getWords("ming.txt");


        generateNameButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String lastName = randomName(xings, mings);
                while (generatedNames.contains(lastName)){
                    lastName = randomName(xings, mings);
                }
                nameNum += 1;
                generatedNames.add(lastName);
                lastNameTextView.setText(lastName);

                nameListTextView.append(nameNum + ". " + lastName + "\n");
                scrollView.fullScroll(ScrollView.FOCUS_DOWN);
            }
        });

    }


    private String[] getWords(String fileName){
        String fileContent = null;
        String[] words = new String[0];

        try {
            AssetManager assetManager = getAssets();
            InputStream is = assetManager.open(fileName);
            int length = 0;
            length = is.available();
            byte[]  buffer = new byte[length];
            is.read(buffer);
            fileContent = new String(buffer, "utf8");
        } catch (Exception e) {
            e.printStackTrace();
            return words;
        }

        words = fileContent.trim().split(" ");

        return words;
    }


    private String randomWord(String[] words){
        int randomIndex = (int) (Math.random()*words.length);
        return words[randomIndex];
    }

    private String randomName(String[] xings, String[] mings){
        String xing = randomWord(xings);
        String ming = randomWord(mings);
        if (Math.random() > 0.5){
            ming += randomWord(mings);
        }
        String lastName = xing + ':' + ming;
        return lastName;
    }

}
