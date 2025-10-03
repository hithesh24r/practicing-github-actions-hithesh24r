const core = require('@actions/core');
 
async function run() { 
  // this is the place where we can add the functionality we need
  core.info('I am a custom JS action');
}
 
run();