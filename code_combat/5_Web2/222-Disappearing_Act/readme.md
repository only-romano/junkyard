## _Disappearing Act_

#### _Legend says:_
> Make elements vanish and appear! Astound your enemies, bewilder your friends.

#### _Goals:_
+ _Hide the image using `.hide()`_
+ _Click `#hideButton`_

#### _Topics:_
+ None

#### _Solutions:_
+ **[HTML](Disappearing_Act.html)**

#### _Rewards:_
+ 60  xp
+ 20 gems

#### _Victory words:_
+ _VANISHED BEFORE YOUR VERY EYES!_

___

### _HINTS_

The `show()` and `hide()` jQuery functions make elements appear and disappear.

#### _`hide()` and `show()`_

`hide` makes an element invisible.

When calling `hide()` on an element, it will make it disappear from the screen!

`show` makes an element visible.

The inverse of this, `show()` will cause the element to reappear in the same fashion it was before it was hidden. (Unless changes were made while it was hidden!)

Hooking into `"click"` events allows you to script up behavior for hiding and redisplaying elements that matter!

**Example:**

```html
<div>
    <h3>Information of Valuability</h3>
    <div class="info">
        Valued information goes here.
    </div>
</div>
<script>
    // Hide all infoDivs at the start of the script.
    $(".infoDiv").hide();
    function showInfoChild() {
        // Show the clicked target's infoDiv.
        $(".infoDiv", this).show()
    }
    $(".infoDiv").parent().on('click', showInfoChild)
</script>
```

___
