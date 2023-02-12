input_string = "edeaaabbccd";

var answer = '';
    
var lists = [input_string[0]];
var cnt = 0;
for (var i = 1; i < input_string.length; i++) {
    if (lists[cnt] != input_string[i]) {
        lists.push(input_string[i]);
        cnt += 1;
    }
}

var answer_list = []
for (var i = 0; i < lists.length; i++) {
    let count  = lists.filter(e => lists[i] === e).length;
    
    if (count > 1 && answer_list.find(e => e == lists[i]) == undefined) {
        answer_list.push(lists[i]);
    }
}

if (answer_list.length == 0) {
    answer = 'N';
}
else {
    answer_list.sort();
    answer = answer_list.join("");
}

console.log(answer);