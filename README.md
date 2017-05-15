Before starting this, I looked through the work of others attempting this. The majority solved the problem using JavaScript.
In my opinion, JavaScript should only be used in validation as an enhancement, and not the only solution. It's far too easy
to turn off JavaScript and then submit an invalid form. Also, I didn't want to do the same thing everyone has done :)

I've solved this using Python and Flask. It's the first time I've used Flask, so it took a little bit over the two hour allocation,
but I thought it was time well spent as I was able to learn a new framework.

To run this;

Open your terminal, and `cd` to this project directory.

Using VirtualEnv (optional, but recommended)
```commandline
pip install virtualenv
virtualenv venv
source venv/bin/activate
```
If you're not using VirtualEnv, start here:
```commandline
pip install -r requirements.ini
export FLASK_APP=main.py
flask run
```

You should then see a message like;
```commandline
 * Serving Flask app "main"
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open your browser to [127.0.0.1:5000](http://127.0.0.1:5000), and there you have it.

# [Form validation problem](https://github.com/springload/form-validation-problem)

We've created this problem to evaluate how developers tackle a real-world problem. If you've been assigned this problem you should spend around **2 hours** working on it. The last thing we want you to do is toil away for days on end!

If you've stumbled across this and want to work at [Springload](https://www.springload.co.nz/) feel free to submit it too. We're always on the lookout for skilled developers.

## Problem definition

Included in this repository is an [index.html](templates/index.html) file that contains a form. You must ensure all of the following rules are met before the form is posted to the (in this case imaginary) server:

* `Email` must be a valid email address.
* `Password` must be longer than 8 characters.
* `Colour` must be selected.
* At least two `Animal`s must be chosen.
* If `Tiger` is one of the chosen `Animal`s then `Type of tiger` is required to be a non-empty string.

## Other requirements

If the form is submitted and an error occurs, the error element's parent should have a CSS `error` class added to it.

```html
<p class="error">
    <label for="field"></label>
    <input id="field" type="text" value="foo">
</p>
```

## The cherry on the cake

Beyond the problem statement, show us the consideration you have given to some or all of the following:

- Documentation
- Accessibility
- Progressive enhancement
- Browser support
- Testing
- Tooling

## Submission

Please email us a link to your fork of this repository, or a zip of your solution to `1337h4x0r@springload.co.nz`.
