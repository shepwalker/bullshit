function checkBullshit(input){
    var array_list = [];
    var test_bullshit = {synergy: 3, visibility: 2, leverage: 1000};
    var foundBullshit = getBullshit(input, test_bullshit);
    for (var prop in foundBullshit){
        var aBullshit = foundBullshit[prop];
        var bullshitLength = prop.length;
        for(i = 0; i < aBullshit.length; i++){
            array_list.push([aBullshit[i], aBullshit[i] + bullshitLength]);
        }
    }
    return array_list;
}

$(document).ready(function() {
    $('#isThisBullshit').highlightWithinTextarea(checkBullshit);
});
