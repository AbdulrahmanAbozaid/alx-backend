import kue from 'kue';

const jobs = [
  {
    phoneNumber: '4153518780',
    message: 'This is the code 1234 to verify your account',
  },
  {
    phoneNumber: '4153518781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153518743',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153538781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153118782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4153718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4159518782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4158718781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4153818782',
    message: 'This is the code 4321 to verify your account',
  },
  {
    phoneNumber: '4154318781',
    message: 'This is the code 4562 to verify your account',
  },
  {
    phoneNumber: '4151218782',
    message: 'This is the code 4321 to verify your account',
  },
];

const push_notification_code_2 = kue.createQueue();

for (const job of jobs) {
  const smsJob = push_notification_code_2.create('sms', job).save((err) => {
    if (!err) {
      console.log('Notification job created:', smsJob.id);
    }
  });

  smsJob
    .on('complete', (result) => {
      console.log(`Notification job ${smsJob.id} completed`);
    })
    .on('failed', (err) => {
      console.log(`Notification job ${smsJob.id} failed: ${err}`);
    })
    .on('progress', (progress, data) => {
      if (progress === 0 || progress === 50)
        console.log(`Notification job #${smsJob.id} ${progress}% complete`);
    });
}
