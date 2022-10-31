use std::collections::HashMap;
use std::convert::TryInto;
use float_eq;

fn main() {
  // let bracket = vec![[1.0,16.0], [8.0,9.0], [5.0,12.0], [4.0,13.0], [6.0,11.0], [3.0,14.0], [7.0,10.0], [2.0,15.0]];
  let bracket_orig = vec![1.0,16.0,8.0,9.0,5.0,12.0,4.0,13.0,6.0,11.0,3.0,14.0,7.0,10.0,2.0,15.0];
  let bracket_zero = update_bracket_zero(bracket_orig);
  let result = get_all_win_probabilities(bracket_zero);
  println!("original p = {}", result.get(&2).unwrap());
  // assert_eq!(bracket, bracket_zero);

  let bracket = vec![1.0,16.0,8.0,9.0,5.0,12.0,4.0,13.0,6.0,11.0,3.0,14.0,7.0,10.0,2.0,15.0];

  let mut two_prob_max : f64 = 0.0;
  let mut i_max : usize = 0;
  let mut j_max : usize = 0;

  for i in 0..bracket.len() {
    for j in 0..i {
      let mut bracket_clone = bracket.clone();
      bracket_clone.swap(i,j);
      let swapped_bracket = update_bracket_zero(bracket_clone);
      let result = get_all_win_probabilities(swapped_bracket);
      let two_prob : f64 = *result.get(&2).unwrap();
      if two_prob > two_prob_max {
        i_max = i;
        j_max = j;
        two_prob_max = two_prob;
      }
    }
  }
  println!("i = {}, j = {}, p = {}", i_max, j_max, two_prob_max);

  // Answer:
  // Swap the 3 and 16 seeds to raise the probability of the 2 seed winning from 0.21603968781701657 to 0.28161919151959297
}


#[allow(dead_code)]
fn get_all_win_probabilities(bracket : Vec<[f64;2]>) -> HashMap<u32,f64> {
  let two_win_probs = get_two_win_probability(&bracket);
  let bracket_two = update_bracket_one(bracket);

  let three_win_probs = get_three_win_probability(&bracket_two, two_win_probs);
  let bracket_three = update_bracket_two(bracket_two);

  let four_win_probs = get_four_win_probability(&bracket_three, three_win_probs);

  // for item in four_win_probs.iter() {
  //   println!("{:?}", item);
  // }
  four_win_probs
}

// fn update_bracket<T : std::fmt::Debug>(bracket : Vec<T>) {
//   let mut arr = [0.0;bracket.len()/2]; // Non constant value, should be stucture array or vector of vectors
//   for idx in (0..bracket.len()).step_by(2) {
//     let temp = [&bracket[idx], &bracket[idx+1]];
//     println!("{:?}", temp);
//   }
//   println!("{:?}", bracket.len());
// }

#[allow(dead_code)]
fn update_bracket_zero(bracket : Vec<f64>) -> Vec<[f64;2]> {
  let mut new_bracket = Vec::new();
  for idx in (0..bracket.len()).step_by(2) {
    let temp : [f64;2] = [bracket[idx], bracket[idx+1]];
    new_bracket.push(temp);
  }
  new_bracket
}

#[allow(dead_code)]
fn update_bracket_one(bracket : Vec<[f64;2]>) -> Vec<[f64;4]> {
  let mut new_bracket = Vec::new();
  for idx in (0..bracket.len()).step_by(2) {
    let temp : [f64;4] = [bracket[idx], bracket[idx+1]].concat().try_into().unwrap();
    new_bracket.push(temp);
  }
  new_bracket
}

#[allow(dead_code)]
fn update_bracket_two(bracket : Vec<[f64;4]>) -> Vec<[f64;8]> {
  let mut new_bracket = Vec::new();
  for idx in (0..bracket.len()).step_by(2) {
    let temp : [f64;8] = [bracket[idx], bracket[idx+1]].concat().try_into().unwrap();
    new_bracket.push(temp);
  }
  new_bracket
}

#[allow(dead_code)]
fn get_two_win_probability(bracket: &Vec<[f64;2]>) -> HashMap<u32,f64> {
  let mut opponent : [f64;2];
  let mut two_win_probs = HashMap::new();
  let mut tot_prob : f64 = 0.0;
  for idx in 0..bracket.len() {
    if idx%2 == 0 {
      opponent = bracket[idx+1];
    } else {
      opponent = bracket[idx-1];
    }
    for i in 0..bracket[idx].len() {
      let team = bracket[idx][i];
      let first_round_opponent = bracket[idx][(-1*(i as i32)+1) as usize];
      let prob = first_round_opponent/(team + first_round_opponent) * (opponent[0]/(opponent[0]+team)*opponent[1]/(opponent[0]+opponent[1]) + opponent[1]/(opponent[1]+team)*opponent[0]/(opponent[0]+opponent[1]));
      two_win_probs.insert(team as u32, prob);
      tot_prob += prob;
    }
    if idx%2 == 1 {
      float_eq::assert_float_eq!(tot_prob, 1.0, rmax <= 20.0*f64::EPSILON);
      tot_prob = 0.0;
    }
  }
  two_win_probs
}

#[allow(dead_code)]
fn get_three_win_probability(bracket: &Vec<[f64;4]>, probabilities: HashMap<u32, f64>) -> HashMap<u32,f64> {
  let mut opponents : [f64;4];
  let mut three_win_probs = HashMap::new();
  let mut tot_prob : f64 = 0.0;

  for idx in 0..bracket.len() {
    if idx%2 == 0 {
      opponents = bracket[idx+1];
    } else {
      opponents = bracket[idx-1];
    }

    for i in 0..bracket[idx].len() {
      let team = bracket[idx][i];
      let mut prob : f64 = 0.0;
      for j in 0..opponents.len() {
        prob += probabilities[&(team as u32)]*probabilities[&(opponents[j] as u32)]*opponents[j]/(team+opponents[j]);
      }
      three_win_probs.insert(team as u32, prob);
      tot_prob += prob;
    }
  }
  float_eq::assert_float_eq!(tot_prob, 2.0, rmax <= 20.0*f64::EPSILON);
  three_win_probs
}

#[allow(dead_code)]
fn get_four_win_probability(bracket: &Vec<[f64;8]>, probabilities: HashMap<u32, f64>) -> HashMap<u32,f64> {
  let mut opponents : [f64;8];
  let mut four_win_probs = HashMap::new();
  let mut tot_prob : f64 = 0.0;

  for idx in 0..bracket.len() {
    if idx%2 == 0 {
      opponents = bracket[idx+1];
    } else {
      opponents = bracket[idx-1];
    }

    for i in 0..bracket[idx].len() {
      let team = bracket[idx][i];
      let mut prob : f64 = 0.0;
      for j in 0..opponents.len() {
        prob += probabilities[&(team as u32)]*probabilities[&(opponents[j] as u32)]*opponents[j]/(team+opponents[j]);
      }
      four_win_probs.insert(team as u32, prob);
      tot_prob += prob;
    }
  }
  float_eq::assert_float_eq!(tot_prob, 1.0, rmax <= 20.0*f64::EPSILON);
  four_win_probs
}



/*
7----|
     |-----|
10---|     |
           |-----
2----|     |
     |-----|
15---|



7----|       p = 10/17
     |----7|
10---|     |
           |-----
2----|     |
     |----2|
15---|

7----|       p = 7/17
     |---10|
10---|     |
           |-----
2----|     |
     |----2|
15---|


7----|       p = (10/12*7/17 + 7/9*10/17) * 15/17 = 0.7064590542099193
     |-7|10|
10---|     |
           |-----2
2----|     |
     |----2|
15---|

p 2-seed making it to final 4
15/17 * 10/12, with probability 7/17 = 0.3027
or
15/17 * 7/9, with probability 10/17 = 0.40369

p = 0.7064590542099192

p 2-seed makes it to final 8 but not 4
15/17 * 2/12 * 7/17 = 0.060553633217993084
or
15/17 * 2/9 * 10/17 = 0.11534025374855825
p = 0.17589388696655134

p 2-seed does not make it to final 8
2/17 = 0.1176470588235294



6----|       p = (10/12*7/17 + 7/9*10/17) * 15/17 = 
     |-6|11|
11---|     |
           |-----
3----|     |
     |-3|14|
14---|       p


7----|
     |-7|10|
10---|     |     p = (10/12*7/17 + 7/9*10/17) * 15/17 = 
           |-----2
2----|     |
     |----2|
15---|       p = 15/17


Probabilities of winning round of 16 and 8

p6  = 11/17 * (14/20*3/17 + 3/9*14/17)
p11 =  6/17 * (14/25*3/17 + 3/14*14/17)
p3  = 14/17 * (11/14*6/17 + 6/9*11/17)
p14 =  3/17 * (11/25*6/17 + 6/20*11/17)

p7  = 10/17 * (2/9 *15/17 + 15/22*2/17)
p10 =  7/17 * (2/12*15/17 + 15/25*2/17)
p2  = 15/17 * (7/9 *10/17 + 10/12*7/17)
p15 =  2/17 * (7/22*10/17 + 10/25*7/17)



Probability that 2-seed wins round of 16, 8, and 4

-6|11|3|14--|
            |---
-----2------|

p = p2 * (6/8*p6 + 11/13*p11 + 3/5*p3 + 14/16*p14) 
  = 15/17 * (7/9 *10/17 + 10/12*7/17) * (6/8*11/17 * (14/20*3/17 + 3/9*14/17) + 11/13*6/17 * (14/25*3/17 + 3/14*14/17) + 3/5*14/17 * (11/14*6/17 + 6/9*11/17) + 14/16*3/17 * (11/25*6/17 + 6/20*11/17)) 
  = 0.4800438163256346

8----|
     |-----|
16---|     |
           |-----
1----|     |
     |-----|
9----|


*/