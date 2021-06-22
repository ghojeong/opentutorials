// Entry File

import hello_word from "./hello.js";
import world_word from "./world.js";

const word = `${hello_word} ${world_word}`;
document.querySelector("#root").innerHTML = word;
