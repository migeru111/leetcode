fn gcd_of_strings(str1: &str, str2: &str) -> String {
    let mut ans = String::from("");
    for i in 0..str1.len()+1 {
        if i == 0 {
            continue
        }
        let mut tmp_str1=String::from("");
        let mut tmp_str2=String::from("");
        
        let tmp_a = &str1[0..i];
        let tmp_a_l=tmp_a.len();
        let str1_l=str1.len();
        let str2_l=str2.len();

        if str1_l % tmp_a_l != 0 {
            continue
        }
        if str2_l % tmp_a_l != 0 {
            continue
        }

        let iter_num_1 = str1_l/tmp_a_l;

        for _j in 0..iter_num_1 {
            tmp_str1=tmp_str1+tmp_a;
        }
        if &tmp_str1 != str1 {
            continue
        }

        let iter_num_2 = str2_l/tmp_a_l;

        for _j in 0..iter_num_2 {
            tmp_str2=tmp_str2+tmp_a;
        }
        if &tmp_str2 != str2 {
            continue
        }
        ans=tmp_a.to_string();
        println!("tmp_a={},tmp_str1={},tmp_str2={}",tmp_a,tmp_str1,tmp_str2)
    }
    return ans
}

fn main() {
    let str1 = String::from("abc");
    let str2 = String::from("abcabc");
    println!("{}", gcd_of_strings(&str1, &str2));
}
