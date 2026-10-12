#include <iostream>
#include <random>

// TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.

int main() {
    int i=0;
    std::default_random_engine gen;
    std::uniform_real_distribution<double> distribution(0.0,
                                                        1.0);

    int num_of_cases_not_equal = 0;

    for (i=0;i<10000000;i++) {
        double x=distribution(gen);
        double y=distribution(gen);
        double z=distribution(gen);

        double value1 = ((x+y)+z);
        double value2 = (x+(y+z));

        if (value1!=value2) {
            num_of_cases_not_equal++;
        }





    }
    std::cout<< (num_of_cases_not_equal*100/10000000) << "%";

    return 0;
}