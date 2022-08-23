//////////////////////////////////////////////////////////////
// Script Name:     XOR-enc.js                              //            
// Author:          Levi von Haxor                          //
// Description:     Symmetric XOR encrytion utilizing two   //
//                  different XOR functions                 //
//////////////////////////////////////////////////////////////

const charList = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'; // The character pool to choose our key from

const charLength = charList.length  

let contents = 'Thanks for checking out this script!'; 

const contentsLength = contents.length;


// The first key method involves a key length == contents length
function xorKey1()
{
    let key = '';

    for (i = 0; i < contentsLength; i++)
    {
        key += charList[Math.floor(Math.random() * charLength)] // We use the floor method since indexing begins at 0 and ends at contentsLength - 1
    };

    return key;
};
// ENSURE YOU SAVE THE KEY! YOU WILL NEED IT TO DECRYPT YOUR CONTENTS!


// The first XOR function uses a key of the same length as the content being encrypted, each content index will XOR with the corresponding key index
function xorEnc1(contents, key)
{
    let xorContents = '';
    
    for (let i =0; i < contentsLength; i++)
    {
        xorContents += String.fromCharCode(contents.charCodeAt(i) ^ key.charCodeAt((i)))     
    };

    return xorContents;
};



// The second key method involves a key of length 1
function xorKey2()
{
    let key = charList[Math.floor(Math.random() * charLength)] // Same floor method here but no for loop

    return key;
};
// ENSURE YOU SAVE THE KEY! YOU WILL NEED IT TO DECRYPT YOUR CONTENTS!


// The second XOR function uses the key of length 1 to XOR with each charCode through the indeces
function xorEnc2(contents, key)
{
    let xorContents = '';

    for (let i = 0; i < contentsLength; i++)
    {
        xorContents += String.fromCharCode(contents.charCodeAt(i) ^ key.charCodeAt(0)) 
    };

    return xorContents;
};




// Method 1

let key1 = xorKey1(); // Key length == Contents length

let xorContents1 = xorEnc1(contents, key1); 

let decContents1 = xorEnc1(xorContents1, key1);


console.log(`Original Contents: ${contents}\n`);

console.log(`Encryption Key: ${key1}\n`);

console.log(`XOR Encrypted Contents: ${xorContents1}\n`);

console.log(`Decrypted Contents: ${decContents1}\n\n`); // To show the symmetric encryption nature of XOR


// Method 2

let key2 = xorKey2(); // Key length == 1

let xorContents2 = xorEnc2(contents, key2);

let decContents2 = xorEnc2(xorContents2, key2);


console.log(`Original Contents: ${contents}\n`);

console.log(`Encryption Key: ${key2}\n`);

console.log(`XOR Encrypted Contents: ${xorContents2}\n`);

console.log(`Decrypted Contents: ${decContents2}`); // To show the symmetric encryption nature of XOR
