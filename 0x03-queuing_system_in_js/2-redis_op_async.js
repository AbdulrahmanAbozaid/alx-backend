import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error('Redis client not connected to the server:', err.message);
});

/**
 * Set a new school in Redis.
 * @param {string} schoolName - The key for the school.
 * @param {string} value - The value to set.
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

/**
 * Display the value of a school from Redis.
 * @param {string} schoolName - The key for the school.
 */
async function displaySchoolValue(schoolName) {
  try {
    const value = await promisify(client.get).bind(client)(schoolName);
    console.log(value);
  } catch (error) {
    console.error('Error retrieving value:', err.message);
    return;
  }
}

displaySchoolValue('ALX');
setNewSchool('ALXSanFrancisco', '100');
displaySchoolValue('ALXSanFrancisco');
