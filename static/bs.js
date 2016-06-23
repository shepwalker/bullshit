//Taken from https://stackoverflow.com/questions/3410464/how-to-find-all-occurrences-of-one-string-in-another-in-javascript
function getIndicesOf(searchStr, str, caseSensitive) {
    var startIndex = 0, searchStrLen = searchStr.length;
    var index, indices = [];
    if (!caseSensitive) {
        str = str.toLowerCase();
        searchStr = searchStr.toLowerCase();
    }
    while ((index = str.indexOf(searchStr, startIndex)) > -1) {
        indices.push(index);
        startIndex = index + searchStrLen;
    }
    return indices;
}

function getBullshit(text, bullshit_list) {
    var bullshit_found = {};
    for(var prop in bullshit_list){
        var result = getIndicesOf(prop, text, false);
        if(result.length > 0){
            bullshit_found[prop] = result;
        }
    }
    return bullshit_found;
}