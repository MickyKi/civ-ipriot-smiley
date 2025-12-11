# Evidence and Knowledge

This document includes instructions and knowledge questions that must be completed to receive a *Competent* grade on this portfolio task.

## 1. Required evidence

### 1.1. Answer all questions in this document

- Each answer should be complete, well-articulated, and within the specified word count limits (if added) for each question.
- Please make sure **all** external sources are properly cited.
- You must **use your own words**. Please include your full chat transcripts if you use generative AI in any way.
- Generative AI hallucinates, is not an authoritative source

### 1.2. Make all the required modifications to the code

- Please follow the instructions in this document to make the changes needed to the code.

- When requested to upload evidence, upload all screenshots to `screenshots/` and embed them in this document. For example:

```markdown
![Example Running Code](screenshots/screenshot1.png)
```

![Sample](screenshots/sample.png)
> Note the `!`, and the use of a relative path.

- You must upload the code into your GitHub repository.
- While you can use a branch, your code should be in main when you submit.
- Upload a zip of this repository to Blackboard when you are ready to submit.
- You will be notified of your result via Blackboard
- However, if using GitHub classrooms, you may also receive additional feedback on GitHub directly

### 1.3. Optional: Use of Raspberry Pi and SenseHat

Raspberry Pi or SenseHat is **optional** for this activity. You can use the included `sense_hat.py` file to simulate the SenseHat on your computer.

If you use a Pi, please **delete** the `sense_hat.py` file.

### 1.4. Accessible version of the code

This project relies on visual patterns that appear on an LED matrix. If you have any accessibility requirements, you can use the `udl/accessible` branch to complete the project. This branch provides an accessible code version that uses text-based patterns instead of visual ones.

Please discuss this with your lecturer before using that branch.

## 2. Specific Tasks & Questions

Address the following tasks and questions based on the code provided in this repository.

### 2.1. Set up the project locally

1. Fork this repository (if not using GitHub Classrooms)
2. Clone your repository locally
3. Run the project locally by executing the `main.py` file
4. Evidence this by providing screenshots of the project directory structure and the output of the `main.py` file

![Local Execution (INSERT YOUR SCREENSHOT)](screenshots/CREATE_A_SCREENSHOT_OF_YOUR_local_setup.png)

If you are running on a Raspberry Pi, you can use the following command to run the project and then screenshot the result:

```bash
ls
python3 main.py
```

### 2.2. Fundamental code comprehension

 Answer each of the following questions **as they relate to that code** supplied by in this repository (ignore `sense_hat.py`):

1. Examine the code for the `smiley.py` file and provide  an example of a variable of each of the following types and their corresponding values (`_` should be replaced with the appropriate values):

   | Type                    | name       | value          |
   | ----------              | ---------- | -------------- |
   | built-in primitive type | white      | 255, 255, 255  |
   | built-in composite type | pixels	    |list; 64 tuples (8x 8)|
   | user-defined type       | self	      |instance of Smiley    |

2. Fill in (`_`) the following table based on the code in `smiley.py`:

   | Object                   | Type                    |
   | ------------             | ----------------------- |
   | self.pixels              | List                    |
   | A member of self.pixels  | Tuple                   |
   | self                     | Smiley                  |

3. Examine the code for `smiley.py`, `sad.py`, and `happy.py`. Give an example of each of the following control structures using an example from **each** of these files. Include the first line and the line range:

   | Control Flow   | File       | First line        | Line range  |
   | ------------   | ---------- | -----------       | ----------- |
   | sequence	      | smiley.py	 |self.pixels = [	   | 14–30       |
   | selection	     | sad.py	    | if wide_open:	    | 17–21       |
   | iteration      |	happy.py	  |for pixel in mouth:|	15–17       |

4. Though everything in Python is an object, it is sometimes said to have four "primitive" types. Examining the three files `smiley.py`, `sad.py`, and `happy.py`, identify which of the following types are used in any of these files, and give an example of each (use an example from the code, if applicable, otherwise provide an example of your own):

   | Type                    | Used? | Example |
   | ----------------------- | ----- | --------|
   |int	                     |Yes	   | 255 (from WHITE = (255, 255, 255))|
   |float	                   |Yes    |	0.25 (from blink(self, delay=0.25) in happy.py) |
   |str	                     |Yes    |	"Draws the mouth feature on a smiley" (docstring in sad.py) |
   |bool	                    |Yes	   | wide_open=True (parameter in draw_eyes methods) |

5. Examining `smiley.py`, provide an example of a class variable and an instance variable (attribute). Explain **why** one is defined as a class variable and the other as an instance variable.

> Your answer here
> (Within smiley.py) YELLOW = (255, 255, 0) is a class variable because it’s written at the top of the class, outside of the method content. Thus it acts like a shared constant — meaning every Smiley object can use it. The value also stays the same no matter how many smileys the user creates. Colours make sense to be categorised as class variables because they don’t change from one object to the next (similarly the could be termed constants).
> By contrast, self.pixels can be categorised as an "instance variable" because it’s created inside the constructor (__init__). Noteworthy, that each smiley object has its own version (i.e., `self.pixels). 

6. Examine `happy.py`, and identify the constructor (initializer) for the `Happy` class:
   1. What is the purpose of a constructor (in general) and this one (in particular)?

   > Your answer here
   >In Python, a constructor (__init__) will run automatically when a new objects created. Its general purpose is to set the object’s starting state up, so it’s ready to be used.
   > In the Happy class, the constructor starts by calling the parent Smiley constructor to build the basic smiley, followed by customising it by drawing the mouth and eyes. This makes sure every Happy object starts by/looks like a happy face.

   2. What statement(s) does it execute (consider the `super` call), and what is the result?

   > Your answer here
   > The constructor executes super().__init__(), which runs the parent Smiley setup and creates the base pixel grids/SenseHat objects.
   > Next, it calls self.draw_mouth() and self.draw_eyes(), which changes the specific pixels by forming a happy mouth and eyes. The outcome: every new Happy object starts with a working smiley appearance that will look cheerful.

### 2.3. Code style

1. What code style is used in the code? Is it likely to be the same as the code style used in the SenseHat? Give to reasons as to why/why not:

> Your answer here
> The code style for the code follows the PEP 8 Python style guide, which is the standard convention for Python and what we use at Nmtafe e.g., lowercase_with_underscores for method names (draw_mouth, draw_eyes), consistent indentation, and docstrings used for functions.

It’s not guaranteed to be the same coding style as the official SenseHat library, because that library could have its own conventions or priorities (i.e., focusing on hardware integration opposed to strict coding styles). 

However, both are Python projects, so it’s likely they share some similar practices and coding styles may overlap.

Reasons:

The smiley code uses PEP 8 conventions (e.g., naming and indentation), which are common in Python projects.

The SenseHat library is also written in Python, so it probably follows similar conventions, but it may differ in places to match hardware, tasks, and performance needs. Thus better to state the likelihood indefinitive opposed to absolute. 

2. List three aspects of this convention you see applied in the code.

> Your answer here
> Method naming/coding style, posits users use lowercase_with_underscores (e.g. draw_mouth, draw_eyes).

Indentation must be consistent (i.e., four spaces per level).

Docstrings i.e., included under classes/methods as this explains their purpose.

3. Give two examples of organizational documentation in the code.

> Your answer here
> Two examples of organizational documentation that are found in the code are:

Module‑level imports and structure (like import time/from smiley, import Smiley at the top), which shows the programmer how the codes organised and what external resources it requires.

Inline comments (e.g., ' #Renders a mouth by blanking the pixels'), which clarify the roles of specific code blocks
### 2.4. Identifying and understanding classes

> Note: Ignore the `sense_hat.py` file when answering the questions below

1. List all the classes you identified in the project. Indicate which classes are base classes and which are subclasses. For subclasses, identify all direct base classes.
  
  Use the following table for your answers:

| Class Name | Super or Sub? | Direct parent(s) |
| ---------- | ------------- | ---------------- |
| Class Name | Super or Sub? | Direct parent(s) |
| Smiley     | Super         | none (no real parent) |
| Sad        | Sub           | Smiley  (real parent) |
| Happy      | Sub           | Smiley (real parent), Blinkable (real parent) |
| Blinkable  | Super         | none             |

2. Explain the concept of abstraction, giving an example from the project (note "implementing an ABC" is **not** in itself an example of abstraction). (Max 150 words)

> Your answer here
>Abstraction refers to the process of simplifying complex systems i.e., focusing only on the key features/hiding unnecessary detail. In this iPRIOT project, the Smiley class is a good example as it manages the underlying pixel grid/SenseHat setup, but users do not need to understand how each is controlled (i.e., LED). Instead, subclasses (such as Happy/Sad) provide clear methods e.g., draw_mouth() or draw_eyes() that represent facial expressions.
> This makes the codes easier to read, decreases related complexity, and allows students/junior developers to work with high‑level concepts rather than low‑level technical tasks and projects.

3. What is the name of the process of deriving from base classes? What is its purpose in this project? (Max 150 words)

> Your answer here
> The process of 'deriving from base classes' is called inheritance. Inheritance allows the reuse and functional extensions by new classes, without having to rewrite code. In this project, Sad and Happy inherit (i.e., from the base class Smiley), which sets up pixel grids and core drawing methods are provided. By inheriting, these subclasses only need to override/add features that make their expressions unique, this is evident by shape of their mouth and blinking behaviour. This reduces duplication, keeps the designs/workstation organised, and makes the program comparatively easier to maintain.
If another emotions were needed, then new subclasses could be quickly created by reusing the same base-logic. Inheritance therefore supports several areas such as; flexibility, clarity, and efficient development in the project tasks.

### 2.5. Compare and contrast classes

Compare and contrast the classes Happy and Sad.

1. What is the key difference between the two classes?
   > Your answer here
   > The Happy classes extend Smiley's by overriding methods resulting in an upward mouth curve drawn and the option to add blinking behaviour, while the Sad classes override the same base methods and result in a downward mouth curve drawn without blinking. There is multiple key differences difference such as the visual expression and how each subclass customises inherited behaviour to represent distinct emotions and behaviours.
   
2. What are the key similarities?
   > Your answer here
   > Both classes inherit features from Smiley, rely on the same pixel grid setup, and are reconfigured via methods, to define facial features. They share the same structure and purpose i.e., representing emotion states through base design variations.
   
3. What difference stands out the most to you and why?
   > Your answer here
   > The overriding mouth‑drawing logic stands out to me the most because it directly changes the emotions semantic representation surrounding for display, and makes the intent/behaviour of each class clear.
   
4. How does this difference affect the functionality of these classes
   > Your answer here
   > It determines the emotional tone which is shown on the SenseHat i.e., happy produces out put that is cheerful, and engaging, while the Sad class produces output resembling a downturned, sombre face. Although it may appear simple, this affects how users will interpret the program’s feedback and demonstrates how inheritance supports expressive variation.

### 2.6. Where is the Sense(Hat) in the code?

1. Which class(es) utilize the functionality of the SenseHat?
   > Your answer here
   > The Smiley superclass utilizes the SenseHat by organising LED pixel grids and providing methods that draw facial features. The Subclasses (such as Happy and Sad) rely on this functionality indirectly through their inheritance.
   
2. Which of these classes directly interact with the SenseHat functionalities?
   > Your answer here
   > The Smiley class is is the class that directly interacts with the SenseHat API. It contains the code that facilitates SenseHat methods to illuminate/show the pixels and display images. 
   
3. Discuss the hiding of the SenseHAT in terms of encapsulation (100-200 Words)
   > Your answer here
   > The hiding of the SenseHat in this project demonstrates encapsulation. By utilising encapsulation we restrict direct access to certain functions and expose it through specific-controlled methods. The Smiley class is the only class found in the code, that can directly interact with the SenseHat, and handle tasks like setting pixels and clearing the display image. Subclasses like Happy and Sad are not required to know the technical details of how the SenseHat is operating; instead, they override/extend the Smiley classes methods which defines their own facial expressions. Further to this, this design helps to isolate hardware interaction, prevent duplication of SenseHat code, and in turn the program is easier to maintain. If the SenseHat changes, only the Smiley class requires the transmission of updates. Noteworthy, the encapsulation process also improves clarity, reduces complexity, and ensures subclasses focuses on behaviour, opposed to low‑level operations.

### 2.7. Sad Smileys Can’t Blink (Or Can They?)

Unlike the `Happy` smiley, the current implementation of the `Sad` smiley does not possess the ability to blink. Let's first explore how blinking has been implemented in the Happy Smiley by examining the blink() method, which takes one argument that determines the duration of the blink.

**Understanding Blink Mechanism:**

1. Does the code's author believe that every `Smiley` should be able to blink? Explain.

> Your answer here
> No, the author does not expect every Smileys blinks. Blinking is limited to certain subclasses (like Happy), while the base Smiley class chooses to focus core features e.g., setting up the pixel grids and drawing expressions. This shows blinking is believed to be optional behaviour rather than a universal requirement.

2. For those smileys that blink, does the author expect them to blink in the same way? Explain.

> Your answer here
> No, the author does not expect blinking smileys to all blink in the same manner. Blinking behaviours defined at the subclass level, thus can be overrided/customised to change how blinking occurs. For example, one smiley might blink at a different rate (faster or slower) or with a different visual effect than another smiley. This design shows that blinkings treated as a flexible behaviour, and allows variation between subclasses rather than enforcing singular, uniformed implementations.

3. Referring to the implementation of blink in the Happy and Sad Smiley classes, give a brief explanation of what polymorphism is.

> Your answer here
> Polymorphism refers to a specific object‑oriented principle where different classes, define their own unique versions of the same method. For example, both Happy and Sad subclasses share inheritance from Smiley and implement their own blinking behaviour. Although the actual method is the same, each one customises how blinking occurs. This allows blink() to be called on by any Smiley object without needing to know its exact type i.e., the correct version still runs. Polymorphism enables flexibility, code reuse, and variable behaviour although there is a consistent interface.

4. How is inheritance used in the blink method, and why is it important for polymorphism?

> Your answer here
> Inheritance allows subclasses (Happy and Sad) to reuse Smiley's base structure while overriding the blink method. This is important for polymorphism i.e., letting the program call blink() on all Smiley objects and running the correct subclass version automatically, triggering different behaviours, without the program needing to know exact object type.


1. **Implement Blink in Sad Class:**

   - Create a new method called `blink` within the Sad class. Ensure you use the same method signature as in the Happy class:

   ```python
    def blink(self, delay=0.25):
        self.sense.clear()     # eyes disappear
        time.sleep(delay)      # short pause
        self.draw_sad_face()   # redraw sad face
   ```

2. **Code Implementation:** Implement the code that allows the Sad smiley to blink. Use the implementation from the Happy Smiley as a reference. Ensure your new method functions similarly by controlling the blink duration through the `delay` argument.

3. **Testing the Implementation:**

- Test the new blink functionality on your Raspberry Pi or within the Python classes provided. You might need to adjust the `main.py` script to incorporate Sad Smiley's new blinking capability.

Include a screenshot of the sad smiley or the modified `main.py`:

![Sad Smiley Blinking](screenshots/sad_blinking.png)

- Observe and document the Sad smiley as it blinks its eyes. Describe any adjustments or issues encountered during implementation.

  > Your answer here

  ### 2.8. If It Walks Like a Duck…

  Previously, you implemented the blink functionality for the Sad smiley without utilizing the class `Blinkable`. Assuming you did not use `Blinkable` (even if you actually did), consider how the Sad smiley could blink similarly to the Happy smiley without this specific class.

  1. **Class Type Analysis:** What kind of class is `Blinkable`? Inspect its superclass for clues about its classification.

     > Your answer here

  2. **Class Implementation:** `Blinkable` is a class intended to be implemented by other classes. What generic term describes this kind of class, which is designed for implementation by others? **Clue**: Notice the lack of any concrete implementation and the naming convention.

  > Your answer here

  3. **OO Principle Identification:** Regarding your answer to question (2), which Object-Oriented (OO) principle does this represent? Choose from the following and justify your answer in 1-2 sentences: Abstraction, Polymorphism, Inheritance, Encapsulation.

  > Your answer here

  4. **Implementation Flexibility:** Explain why you could grant the Sad Smiley a blinking feature similar to the Happy Smiley's implementation, even without directly using `Blinkable`.

  > Your answer here

  5. **Concept and Language Specificity:** In relation to your response to question (4), what is this capability known as, and why is it feasible in Python and many other dynamically typed languages but not in most statically typed programming languages like C#? **Clue** This concept is hinted at in the title of this section.

  > Your answer here

  ***

  ## 3. Refactoring

  ### 3.1. Does a Smiley Have to Be Yellow?

  While our current implementation predominantly features yellow smileys, emotional expressions like sickness or anger typically utilize colors like green, red, or orange. We'll explore the feasibility of integrating these colors into our smileys.

  1. **Defined Colors and Their Location:**

     1. Which colors are defined and in which class(s)?
        > Your answer here
     2. What type of variables hold these colors? Are the values expected to change during the program's execution? Explain your answer.
        > Your answer here
     3. Add the color blue to the appropriate class using the appropriate format and values.

  2. **Usage of Color Variables:**

     1. In which classes are the color variables used?
        > Your answer here

  3. **Simple Method to Change Colors:**
  4. What is the easiest way you can think to change the smileys to green? Easiest, not necessarily the best!
     > Your answer here



  ### 3.2. Flexible Colors – Step 1

  Changing the color of the smileys once is straightforward, but it isn't very flexible. To facilitate various colors for smileys, it is advisable not to hardcode values in any class. This approach was identified earlier as a necessary change. Let's start by removing the built-in assumptions about color in our classes.

  1. **Add a method called `complexion` to the `Smiley` class:** Implement this instance method to return `self.YELLOW`. Using the term "complexion" instead of "color" provides a more abstract terminology that focuses on the meaning rather than implementation.

  2. **Refactor subclasses to use the `complexion` method:** Modify any subclass that directly accesses the color variable to instead utilize the new `complexion` method. This ensures that color handling is centralized and can be easily modified in the future.

  3. **Determine the applicable Object-Oriented principle:** Consider whether Abstraction, Polymorphism, Inheritance, or Encapsulation best applies to the modifications made in this step.

  4. **Verify the implementation:** Ensure that the modifications function as expected. The smileys should still display in yellow, confirming that the new method correctly replaces the direct color references.

  This step is crucial for setting up a more flexible system for color management in the smiley display logic, allowing for easy adjustments and extensions in the future.

  ### 3.3. Flexible Colors – Step 2

  Having removed the hardcoded color values, we now enhance the base class to support dynamic color assignments more effectively.

  1. **Modify the `__init__()` method in the `Smiley` class:** Introduce a default argument named `complexion` and assign `YELLOW` as its default value. This allows the instantiation of smileys with customizable colors.

  2. **Introduce a new instance variable:** Create a variable called `my_complexion` and assign the `complexion` parameter to it. This step ensures that each smiley instance can maintain its own color state.

  3. **Rationale for `my_complexion`:** Using a distinct instance variable like `my_complexion` avoids potential conflicts with the method parameter names and clarifies that it is an attribute specific to the object.

  4. **Bulk rename:** We want to update our grid to use the value of complexion, but we have so many `Y`'s in the grid. Use your IDE's refactoring tool to rename all instances of the **symbol** `Y` to `X`. Where `X` is the value of the `complexion` variable. Include a screenshot evidencing you have found the correct refactor tool and the changes made.

  ![Bulk Rename](screenshots/bulk_rename.png)

  5. **Update the `complexion` method:** Adjust this method to return `self.my_complexion`, ensuring that whatever color is assigned during instantiation is what the smiley displays.

  6. **Verification:** Run the updated code to confirm that Smileys still defaults to yellow unless specified otherwise.

  ### 3.4. Flexible Colors – Step 3

  With the foundational changes in place, it's now possible to implement varied smiley colors for different emotional expressions.

  1. **Adjust the `Sad` class initialization:** In the `Sad` class's initializer method, change the superclass call to include the `complexion` argument with the value `self.BLUE`, as shown:

     ```python
     super().__init__(complexion=self.BLUE)
     ```

  2. **Test color functionality for the Sad smiley:** Execute the program to verify that the Sad smiley now appears blue.

  3. **Ensure the Happy smiley remains yellow:** Confirm that changes to the Sad smiley do not affect the default color of the Happy smiley, which should still display in yellow.

  4. **Design and Implement An Angry Smiley:** Create an Angry smiley class that inherits from the `Smiley` class. Set the color of the Angry smiley to red by passing `self.RED` as the `complexion` argument in the superclass call.

  ***
