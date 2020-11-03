$('.btn-minuse').on('click', function () {
    $(this).parent().siblings('input').val(parseInt($(this).parent().siblings('input').val()) - 1)
})

$('.btn-pluss').on('click', function () {
    $(this).parent().siblings('input').val(parseInt($(this).parent().siblings('input').val()) + 1)
})

/* access local storage
$('.btn-add').on('click', function () {
    // from the 'add button' up to find other values
    var itemName = $(this).parent().siblings(".modal-header").children(".modal-title").text()
    var itemID = parseInt($(this).siblings(".float-left").children(".input-group").children(".item").attr("id"), 10)
    var count = parseInt($(this).siblings(".float-left").children(".input-group").children('input').val(), 10)
    addItems(itemID, count)
    alert("Added " + count + " of " +
        itemName + " itemID: " + itemID)
})
*/


// local storage
// to access it
// localStorage.getItem("itemInfo")
/*
var addItems = function (itemID, count) {
    // retrieve it (Or create a blank array if there isn't any info saved yet),
    var items = JSON.parse(localStorage.getItem('itemInfo')) || [];
    items.push({
        itemID: itemID,
        count: count
    });
    localStorage.setItem('itemInfo', JSON.stringify(items));
}
*/

/* 
// local storage
var addItems = function (itemID, count) {
    // retrieve it (Or create a blank array if there isn't any info saved yet),
    var items = JSON.parse(localStorage.getItem('items')) || [];
    items.push({
        itemID: itemID,
        count: count
    });
    localStorage.setItem('items', JSON.stringify(items));
}
*/


// if items have itemID, count(new) = count(old) + count(added), else push directly

// cookies
$('.btn-add').on('click', function () {
    // from the 'add button' up to find other values
    var itemName = $(this).parent().siblings(".modal-header").children(".modal-title").text()
    var itemID = parseInt($(this).siblings(".float-left").children(".input-group").children(".item").attr("id"), 10)
    var count = parseInt($(this).siblings(".float-left").children(".input-group").children('input').val(), 10)
    // addItems(itemID, count)



    addItemsToList(addItem(itemID, count));
    alert("Added " + count + " of " +
        itemName + " itemID: " + itemID);
})


/**
 * add item to list
 * itemsList is stored as a cookie
 * return json file tthat contains all the items, as a json string
 * @param {} itemJSON 
 */

function addItemsToList(itemJSON) {
    // retrieve it (Or create a blank array if there isn't any info saved yet),
    // get cookie, push, new cookie

    var items = JSON.parse(getCookie("itemsList")) || [];
    if (items[0] == null) {
        items.pop();
    }

    var addedStatus = false;
    // check if this type of item had been added, then add to count
    for (i = 0; i < items.length; i++) {
        if (items[i].itemID == itemJSON.itemID) {
            items[i].count += itemJSON.count;
            addedStatus = true;
        };
    };

    if (addedStatus == false) {
        // console.log(JSON.stringify(items));
        items.push(itemJSON);
    }

    // console.log(JSON.stringify(items));
    var values = JSON.stringify(items);
    setCookie("itemsList", values, 7);
    // for testing
}

/**
 * return list of items without Duplicates
 * @param {*} list 
 */
function checkDuplicates(list) {

}

function hasDuplicates() {
    var items = JSON.parse(getCookie("itemsList"));
    for (i = 0; i < items.length; i++) {
        var checkThisValue = items[i].itemID;
        for (j = i + 1; j < items.length; j++) {
            if (checkThisValue == items[j].itemID) {
                return true;
            }
        }
    }
    return false;
}




function setCookie(cname, cvalue, exdays) {
    var d = new Date();
    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
    var expires = "expires=" + d.toUTCString();
    document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function eraseCookie(name) {
    document.cookie = name + '=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    console.log("eraseCookie");
}



/**
 * return item in json
 * @param {ID of item} itemID 
 * @param {how many of these item} count 
 */
var addItem = function (itemID, count) {
    // var obj = ;
    // return JSON.stringify(obj);
    return {
        itemID: itemID,
        count: count
    };
}

/**
 * 
 * @param {} itemID id of the item
 */
function removeItemFromCookie(itemID) {
    var items = JSON.parse(getCookie("itemsList"));
    for (i = 0; i < items.length; i++) {
        if (items[i].itemID == itemID) {
            items.remove(i);
        };
    };
    // console.log(items);
    var values = JSON.stringify(items);
    setCookie("itemsList", values, 7);
}

function changeCount(itemID, newCount) {
    var items = JSON.parse(getCookie("itemsList"));
    for (i = 0; i < items.length; i++) {
        if (items[i].itemID == itemID) {
            items[i].count = newCount;
        };
    };
    var values = JSON.stringify(items);
    setCookie("itemsList", values, 7);
}

/**
 * helper function to remove js array element
 * @param {} from 
 * @param {*} to 
 */
// Array Remove - By John Resig (MIT Licensed)
Array.prototype.remove = function (from, to) {
    var rest = this.slice((to || from) + 1 || this.length);
    this.length = from < 0 ? this.length + from : from;
    return this.push.apply(this, rest);
};

function checkEmptyItemsListCookie() {
    var values = getCookie("itemsList");
    if (values == "") {
        return true;
    }
    return false;
}