use std::thread;
use std::sync::mpsc;
use rand::{Rng, thread_rng};
use rand::distributions::Uniform;

fn run() -> bool {
    let mut rng = thread_rng();
    let dist = Uniform::new(0.0, 1.0);
    loop {
        let mut sum = rng.sample(dist) - 0.232048;
        if sum > 0.5 {
            return true
        }
        sum -= rng.sample(dist);
        if sum < -0.5 {
            return false
        }
    }
}

fn main() {
    let robot_1_wins = 0;
    let robot_2_wins = 0;

    let n: i64 = 1e2 as i64;
    let (tx, rx) = mpsc::channel::<bool>();


    let handle = thread::spawn(move || {
        for _ in 0..n {
            tx.send(run()).unwrap()
        }
    });

    for received in rx {
        println!("Got: {}", received);
    }

    handle.join().unwrap();
    println!("robot_1_wins = {}", robot_1_wins);
    println!("robot_2_wins = {}", robot_2_wins);
}