package com.example.darren.umanage;

import android.support.test.rule.ActivityTestRule;

import org.junit.Rule;
import org.junit.Test;

import static android.support.test.espresso.Espresso.onView;
import static android.support.test.espresso.action.ViewActions.clearText;
import static android.support.test.espresso.action.ViewActions.click;
import static android.support.test.espresso.action.ViewActions.closeSoftKeyboard;
import static android.support.test.espresso.action.ViewActions.typeText;
import static android.support.test.espresso.assertion.ViewAssertions.matches;
import static android.support.test.espresso.matcher.ViewMatchers.withId;
import static android.support.test.espresso.matcher.ViewMatchers.withText;

/**
 * Created by Darren on 4/28/2016.
 */
public class LoginTest {

    @Rule
    public ActivityTestRule<LoginActivity> mActivityRule =
            new ActivityTestRule<>(LoginActivity.class);

    @Test
    public void validEmailInputTest(){
        onView(withId(R.id.email)).perform(click())
                .perform(clearText())
                .perform(typeText("test"));
        onView(withId(R.id.email)).check(matches(withText("test")));
    }

    @Test
    public void validPasswordInputTest(){
        onView(withId(R.id.password)).perform(click())
                .perform(clearText())
                .perform(typeText("123abc!@#"));
        onView(withId(R.id.password)).check(matches(withText("123abc!@#")));
    }
}
